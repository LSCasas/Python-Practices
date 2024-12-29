def create_file(file_name, content=None):
    """
    Creates a new file or overwrites an existing file with optional content.

    Parameters:
        file_name (str): The name of the file to be created.
        content (str, optional): The content to write into the file. If None, an empty file is created.
            Defaults to None.

    Raises:
        FileExistsError: If the file already exists and `content` is None.
    """
    mode = "w" if content else "x"
    file = open(file_name, mode)
    if content:
        file.write(content)
    file.close()

def modify_file(file_name, content, overwrite=False):
    """
    Modifies an existing file by appending or overwriting content.

    Parameters:
        file_name (str): The name of the file to modify.
        content (str): The content to write into the file.
        overwrite (bool, optional): Whether to overwrite the file's existing content.
            If False, the content is appended to the file. Defaults to False.

    Raises:
        FileNotFoundError: If the specified file does not exist.
    """
    mode = "w" if overwrite else "a"
    file = open(file_name, mode)
    file.write(content)
    file.close()





create_file("example.txt", "Contenido del archivo") #Crea el archivo con contenido
create_file("example2.txt") #Crea el archivo sin contenido

modify_file("example.txt", "Este contenido fue sobre escrito", overwrite=True)
modify_file("example2.txt", "Este contenido fue adicionado")
