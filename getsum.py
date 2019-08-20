# @Created Time: 2019.07.16
# @author: hyumaio

import hashlib
import os

import click


@click.command()
@click.option('--file', '-f', help='Choose a file, use ABSOLUTE file path.', )
@click.option('--mode', '-m', default='md5', help='Choose a mode from [1:MD5, 2:SHA1, 3:SHA256], if not choose, "MD5" will be the default digest mode.')
def main(file, mode):
    # 计算文件的哈希值

    if not file:
        click.echo("Use -f/--file to upload a file!!!")
        return
    if not os.path.isabs(file):
        file = os.path.abspath(file)
    if not os.path.exists(file):
        click.echo('Seems this file is not exists!!!')
        return
    if not os.path.isfile(file):
        click.echo('Not a file!!!')
        return

    if mode == '1' or mode.upper() == 'MD5' or mode == 1:
        mode = 'MD5'
        mode_ = hashlib.md5()
    elif mode == '2' or mode.upper() == 'SHA1' or mode == 2:
        mode = 'SHA1'
        mode_ = hashlib.sha1()
    elif mode == '3' or mode.upper() == 'SHA256' or mode == 3:
        mode = 'SHA256'
        mode_ = hashlib.sha256()
    else:
        click.echo('NOT A INVALID MODE')
        return

    with open(file, 'rb') as f:
        mode_.update(f.read())

    rv = mode_.hexdigest()

    click.echo('--' * 40)
    click.echo('FILE: {}'.format(file))
    click.echo('MODE: {}'.format(mode))
    click.echo('--' * 40)
    click.echo('RESULT: {}'.format(rv))
    click.echo('--' * 40)

    return rv


if __name__ == '__main__':
    main()
    # test
    # r = main('/Users/gcc/Projects/my/3_Python/file_sha256/main.py')
    # print(r)
