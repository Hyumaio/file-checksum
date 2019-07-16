# @Created Time: 2019.07.16
# @Lately Changed: 2019.07.16
# @author: hyumaio

import hashlib
import os

import click


@click.command()
@click.option('--file', '-f', help='Choose a file, use ABSOLUTE file path.', )
@click.option('--mode', '-m', default='md5', help='Choose a mode from [1:md5, 2:sha1, 3:sha256], if not choose, "md5" will be the default '
                                                  'digest '
                                                  'mode.')
@click.option('--value', '-v', help='The original digest value')
def main(file, mode, value):
    click.echo('UR file is: {}'.format(file))
    click.echo('UR mode is: {}'.format(mode))
    click.echo('UR orginal digest result is: {}'.format(value))
    if not value:
        click.echo('Use -v/--value to upload a original digest result!!!')
        return
    value = value.strip()

    if not file:
        click.echo("Use -f/--file to upload a file!!!")
        return
    if not os.path.isabs(file):
        file = os.path.abspath(file)
    if not os.path.exists(file):
        click.echo('seems not exists this file!!!')
        return
    if not os.path.isfile(file):
        click.echo('Not a file!!!')
        return

    if mode == '1' or mode == 'md5' or mode == 1:
        mode = 'md5'
        mode_ = hashlib.md5()
    elif mode == '2' or mode == 'sha1' or mode == 2:
        mode = 'sha1'
        mode_ = hashlib.sha1()
    elif mode == '3' or mode == 'sha256' or mode == 3:
        mode = 'sha256'
        mode_ = hashlib.sha256()
    else:
        click.echo('NOT A INVALID MODE')
        return

    with open(file, 'rb') as f:
        mode_.update(f.read())

    rv = mode_.hexdigest()

    click.echo('--' * 20)
    click.echo('The current digest mode is {}'.format(mode))
    click.echo('Your digest result is {}'.format(rv))
    click.echo('The original digest result is {}'.format(value))
    if rv == value:
        click.echo('\nCHECK PASSED!!! SAFE FILE!!!')
    else:
        click.echo('\nWRONG!!! THE FILE IS NOT THE ORIGINAL FILE!!!')
    return mode_.hexdigest()


if __name__ == '__main__':
    main()
    # test
    # r = main('/Users/gcc/Projects/my/3_Python/file_sha256/main.py')
    # print(r)
