
def get_input():
    f = open('07/input.txt')
    return f.read().splitlines()


class FileSystem():
    def __init__(self):
        self.filesystem = {"home": {}}
        self.current_dir = ["home"]

    def get_current_dir(self):
        tmp = None
        for dir in self.current_dir:
            # highly relying on mutability
            if tmp:
                tmp = tmp[dir]
            else:
                tmp = self.filesystem[dir]
        return tmp

    def cd(self, value):
        if value == '/':
            self.current_dir = ["home"]
        elif value == '..' and self.current_dir != ['home']:
            self.current_dir.pop()
        else:
            dir = self.get_current_dir()
            self.current_dir.append(value)
            dir[value] = {}


    def ls(self, contents):
        dir = self.get_current_dir()
        for content in contents:
            if content[:3] != 'dir' and content[0] != '$':
                dir[content.split(' ')[1]] = int(content.split(' ')[0])


def crawler(fs, sizes, dir, cut_off_value = None):
    fs = fs[dir]
    size = sum([fs[x] for x in fs.keys() if type(fs[x]) == int])
    for key in fs.keys():
        b = 0
        if type(fs[key]) == dict:
            a, b = crawler(fs, sizes, key)
            size += b
            #breakpoint()

    sizes.append(size)
    return sizes, size


if __name__ == "__main__":
    input = get_input()
    file_system = FileSystem()

    input_length = len(input)
    i = 0
    while i < input_length:
        if input[i][0:4] == '$ cd':
            file_system.cd(input[i][5:])
        elif input[i][0:4] == '$ ls':
            # determine no of lines returned from ls
            j = 1
            while i+j < input_length:
                if input[i+j][0] == '$':
                    break
                j += 1
            file_system.ls(input[(i+1):(i+1)+j])
            i += j-1

        i += 1

    sizes = []
    sizes, x = crawler(file_system.filesystem, sizes, 'home')

    print(f'anwser 1: {sum([x for x in sizes if x < 100000 ])}')

    room_needed = 30000000 - (70000000 - max(sizes))
    suitable_dirs = [x for x in sizes if x > room_needed]

    print(f'anwser 2: {min(suitable_dirs)}')
