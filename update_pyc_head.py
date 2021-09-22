import binascii


class UpdatePycHead:
    """
    update pyc head
    """
    @staticmethod
    def hexadecimal_read_file(filename):
        """convert the file to hexadecimal
        """
        byte_list = []

        with open(f'{filename}', 'rb') as f:

            byte = f.read(1)
            while byte:
                byte_list.append('%02x' % (ord(byte)))
                byte = f.read(1)
            f.close()

        return byte_list

    def correct_the_data(self, filename):
        """get your papers right
        """
        struct = self.hexadecimal_read_file('struct')
        norm = self.hexadecimal_read_file(filename)

        for i in range(16):
            norm.insert(i, struct[i])

        return norm

    def restore_file(self, filename):
        """restore hexadecimal byte to file
        """
        norm = self.correct_the_data(filename)
        pyc_name = filename.split(".")[0]
        with open(f'{pyc_name}.pyc', 'wb') as f:
            for byte in norm:
                ascii_byte = binascii.a2b_hex(byte)
                f.write(ascii_byte)
            f.close()
