from proxy.txt_reader import TxtReader
from proxy.txt_writer import TxtWriter


class TxtProxyWriterReader:
    def __init__(self, file_path):
        self.__result = ''
        self.__is_actual = False
        self.__txt_reader = TxtReader(file_path)
        self.__txt_writer = TxtWriter(file_path)

    def read_file(self):
        if self.__is_actual:
            return self.__result
        else:
            self.__result = self.__txt_reader.read()
            self.__is_actual = True
            return self.__result

    def write_file(self):
        self.__result = self.__txt_writer.write('Cool code5')
        self.__is_actual = False


if __name__ == '__main__':
    proxy_reader_writer = TxtProxyWriterReader('my_file.txt')
    # print(proxy_reader.read_file())
    # print('\n')
    print(proxy_reader_writer.read_file())
    proxy_reader_writer.write_file()
    print(proxy_reader_writer.read_file())
