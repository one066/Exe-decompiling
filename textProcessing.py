import binascii

class text_processing:

    def hexadecimal_read_file(self, filename):
        """
        Convert the file to hexadecimal
        """

        byteList = []

        with open(f'{filename}', 'rb') as f:

            byte = f.read(1)
            while byte:
                byteList.append('%02x' % (ord(byte)))
                byte = f.read(1)
            f.close()

        return byteList

    def correct_the_data(self, filename):
        '''
        Get your papers right
        '''

        struct = self.hexadecimal_read_file('struct')
        norm = self.hexadecimal_read_file(filename)

        for i in range(len(norm)):
            if struct[i] == 'e3':
                break
            norm.insert(i, struct[i])

        return norm

    def restore_file(self, filename):
        '''
        Restore hexadecimal byte to file
        '''

        norm = self.correct_the_data(filename)
        with open(f'{filename.split(".")[0]}.pyc', 'wb') as f:
            for byte in norm:
                ascii_byte = binascii.a2b_hex(byte)
                f.write(ascii_byte)
            f.close()

if __name__ == '__main__':
    text_processing().restore_file('zhishu_0715')
