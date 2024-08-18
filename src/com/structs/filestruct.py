class FileStruct:
    """
    A structure that represents an incoming file.
    Will contain the file's bytes as well as attributes from its metadata.
    """

    def __init__(self, attribute_map: dict[str, str], data_bytes: bytearray) -> None:
        """
        Args:
            attribute_map(dict(str, str)): A map of attribute names and their values
            data_bytes(bytearray): The bytes that represent the data
        """
        self.__attribute_map = attribute_map
        self.__data_bytes = data_bytes

    def get_attribute_map(self) -> dict[str, str]:
        """
        Getter for retrieving the map of attribute names and their values
        
        Returns:
            dict(str, str): The map of attribute names and their values
        """
        return self.__attribute_map

    def get_data_bytes(self) -> bytearray:
        """
        Getter for retrieving the byte array representing the data
        
        Returns:
            bytearray: The byte array representation of the data
        """
        return self.__data_bytes
