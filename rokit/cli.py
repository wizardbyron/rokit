from __future__ import absolute_import
import click
import requests
import sys
import csv
from .__version__ import __version__
from .util import pass_tag, fail_tag, highlight, is_valid_url


def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo('version: %s' % __version__)
    ctx.exit()


def highlight_matched_url(source, target):
    return highlight(source) if source == target else source


def parse_redirect_chain(response):
    return list(map(lambda item: item.headers['Location'], response.history))


def highlight_redirect_chain(redirect_chain, target):
    return list(map(lambda item: highlight_matched_url(item, target), redirect_chain))


def print_redirect_chain(redirect_chain):
    click.echo('Redirect %s time(s): %s ' %
               (len(redirect_chain)-1, ' -> '.join(redirect_chain)))


def is_argument_valid(source, target):
    return is_valid_url(source) or is_valid_url(target)


def cli_file(file):
    is_pass = True
    with open(file) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            is_pass = is_pass and cli_url(quote(row[0]), quote(row[1]))
    return is_pass


@click.command()
@click.option('--version', '-v',
              is_flag=True,
              callback=print_version,
              expose_value=False,
              is_eager=True,
              help='Show the version of rokit.')
@click.argument('source', required=False)
@click.argument('target', required=False)
@click.pass_context
def cli(ctx, source, target):
    is_pass = True
    if is_argument_valid(source, target):
        is_pass = cli_url(source, target)
    elif source is not None:
        is_pass = cli_file(source)
    else:
        click.echo(ctx.get_help())
    click.echo('%s' % is_pass)
    sys.exit() if is_pass else sys.exit(1)


def cli_url(source, target):
    is_found = True
    response = requests.get(source)
    redirect_chain = parse_redirect_chain(response)
    redirect_chain_highlighted = [source] + \
        highlight_redirect_chain(redirect_chain, target)
    print_redirect_chain(redirect_chain_highlighted)
    if target != None:
        is_url_found = highlight(target) in redirect_chain_highlighted
        result_msg = ' Request to %s will %s redirect to %s' % (
            source, '' if is_url_found else 'not', target)
        if is_url_found:
            click.echo(pass_tag(result_msg))
            is_found = True
        else:
            click.echo(fail_tag(result_msg))
            is_found = False
    return is_found
