label mod_loader:
    init python:
        import os
        

        # Function to prompt the player for a filename and jump to the corresponding label
        def prompt_for_label():
            # Ask for the name of the label file
            filename = renpy.input("Enter the filename (without .rpy extension): ").strip()

            # Construct the full path to the filename the player entered
            file_path = os.path.join(renpy.config.gamedir, 'scripts', f'{filename}.rpy')


            # Check if the file exists
            if os.path.exists(file_path):
                # Check if the file defines a label, we will assume the label is the same as the file name
                label_name = filename  # The label should be the same as the file name
                renpy.say("player", f"Loading the label from {filename}.rpy...")
                renpy.jump(label_name)  # Jump to the label defined in the specified script file
            else:
                renpy.say("player", f"Error: The file '{filename}.rpy' does not exist.")
                renpy.jump('start')  # Jump back to the start or any default label

label start:
    "Please enter the name of a .rpy file you want to load."

    python:
        # Prompt the player to enter the filename
        prompt_for_label()

    return
