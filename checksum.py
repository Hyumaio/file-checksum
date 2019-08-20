# @Created Time: 2019.07.16
# @author: hyumaio

import hashlib
import os

import click


@click.command()
@click.option('--file', '-f', help='Choose a file, use ABSOLUTE file path.', )
@click.option('--mode', '-m', default='MD5', help='Choose a mode from [1:MD5, 2:SHA1, 3:SHA256], if not choose, "MD5" will be the default digest mode.')
@click.option('--value', '-v', help='The original digest value')
def main(file, mode, value):
    # 比较文件的哈希值是否与给出的哈希值一致，即校验文件是否是源文件

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
    click.echo('DIGEST: {}'.format(value))
    click.echo('--' * 40)
    click.echo('RESULT: {}'.format(rv))
    click.echo('--' * 40)

    if rv.lower() == value.lower():
        click.echo('\nCHECK PASSED!!! SAFE FILE!!!')
    else:
        click.echo('\nWRONG!!! THIS FILE HAS BEEN CHANGED BY SOMEONE!!!')
    return rv


if __name__ == '__main__':
    main()
    # test
    # r = main('/Users/gcc/Projects/my/3_Python/file_sha256/main.py')
    # print(r)
