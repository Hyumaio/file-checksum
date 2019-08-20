# @Created Time: 2019.07.16
# @author: hyumaio

import hashlib
import os
import traceback
import click


@click.command()
@click.option('--file', '-f', help='上传文件，请使用绝对路径。')
@click.option('--mode', '-m', default='MD5', help='参考：[1:MD5, 2:SHA1, 3:SHA256]，"MD5" 是默认 digest 模式。')
@click.option('--value', '-v', help='原始 hash')
def main(file, mode, value):
    # 1. 比较文件的哈希值是否与给出的哈希值一致，即校验文件是否是源文件
    # 2. 计算文件的哈希值
    try:
        # 分隔符
        cut = '---' * 40
        click.echo(cut)


        if not file:
            click.echo("ERROR: 使用 -f/--file 参数指定文件！")
            click.echo(cut)
            return False
        if not os.path.isabs(file):
            file = os.path.abspath(file)
        if not os.path.exists(file):
            click.echo('ERROR: {} 文件不存在!'.format(file))
            click.echo(cut)
            return False
        if not os.path.isfile(file):
            click.echo('ERROR: {} 不是一个文件!'.format(file))
            click.echo(cut)
            return False

        # 是否采用校验模式，默认为 True
        check_ = True

        # 没有指定 value 时，计算哈希值
        if not value:
            click.echo('正在采用计算 hash 模式。')
            click.echo('如果想要使用校验 hash 模式，请使用 -v/--value 参数指定原始 hash 值。')
            check_ = False
        # 指定了 value 时，校验哈希值
        else:
            click.echo('正在采用校验 hash 模式。')
            click.echo('如果想要使用计算 hash 模式，请不要使用 -v/--value 参数。')
            value = value.strip()

        # 判断 mode
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
            click.echo('ERROR: {} 不是一个有效的 digest 模式, 参考：[1:MD5, 2:SHA1, 3:SHA256]'.format(mode))
            click.echo(cut)
            return False

        # get digest result
        with open(file, 'rb') as f:
            mode_.update(f.read())
        rv = mode_.hexdigest()

        # echo 本次处理信息
        click.echo(cut)
        click.echo('目标文件: {}'.format(file))
        click.echo('digest 模式: {}'.format(mode))
        click.echo('传入的 hash 值: {}'.format(value))
        click.echo(cut)
        click.echo('计算得到的 hash 值: {}'.format(rv))

        # 如果是走的校验模式，还需要执行校验逻辑
        if check_:
            if rv.lower() == value.lower():
                click.echo('校验通过，安全的文件。')
            else:
                click.echo('WARNING: 校验失败，文件已被篡改，请谨慎使用！！！')

        click.echo(cut)
        return True
    except Exception as e:
        click.echo("ERROR: 遭遇未知错误，请联系管理员解决：{}, {}".format(e, traceback.format_exc()))
        click.echo(cut)
        return False


if __name__ == '__main__':
    main()
    # test
    # r = main('/Users/gcc/Projects/my/3_Python/file_sha256/main.py')
    # print(r)
