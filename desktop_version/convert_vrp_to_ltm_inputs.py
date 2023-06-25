import os
import sys

if __name__ != '__main__':
    raise ImportError('do not import')

if len(sys.argv) != 2:
    print('Needs exactly 1 argument as input file.')
    sys.exit(1)

base_name = os.path.splitext(sys.argv[1])[0]

with open(sys.argv[1], 'r') as in_file:
    with open(base_name + '_ltm_inputs.txt', 'a') as out_file:
        for line in in_file:
            # strip trailing pipe and last comma
            line = line[:-2]
            keys = []

            for action in line.split(','):
                match action:
                    case 'action_with_text_hold':
                        keys.append('76') # V
                    case 'action_no_text_hold':
                        keys.append('20') # space
                    case 'left':
                        keys.append('61') # a
                    case 'right':
                        keys.append('64') # d
                    case 'restart':
                        keys.append('72') # r
                    case 'interact':
                        keys.append('65') # e
                    case '':
                        pass
                    case _:
                        raise NotImplementedError(f'action {action} not supported')

            out = '|K{0}|\n'.format(':'.join(keys))
            out_file.write(out)
