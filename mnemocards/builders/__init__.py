
from .markdown_card_builder import MarkdownCardBuilder
from .vocabulary_builder import VocabularyBuilder


_BUILDERS = {
    "markdown_card": MarkdownCardBuilder()
}


def get_builder(builder_type):
    return _BUILDERS[builder_type]

