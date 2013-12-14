from os import makedirs
from os.path import dirname, exists, join
from sys import exit

from ..utils import LOG
from ..utils.text import mark_for_translation as _


def write_preview(file_item, base_path):
    """

    """
    file_path = join(base_path, file_item.name.lstrip("/"))
    dir_path = dirname(file_path)
    if not exists(dir_path):
        makedirs(dir_path)
    with open(file_path, 'w') as f:
        f.write(file_item.content)


def bw_items(repo, args):
    node = repo.get_node(args.node)
    if args.file_preview_path:
        if exists(args.file_preview_path):
            LOG.error(_(
                "not writing to existing path: {}"
            ).format(args.file_preview_path))
            exit(1)
        for item in node.items:
            if not item.id.startswith("file:"):
                continue
            if item.attributes['content_type'] == 'binary':
                LOG.warning(_(
                    "skipping binary file {}..."
                ).format(item.name))
                continue
            LOG.info(_(
                "writing {}..."
            ).format(join(
                args.file_preview_path,
                item.name.lstrip("/"),
            )))
            write_preview(item, args.file_preview_path)
    else:
        for item in node.items:
            if args.file_preview_path:
                pass
            if args.show_repr:
                yield repr(item)
            else:
                yield str(item)
