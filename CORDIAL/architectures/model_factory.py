#!/usr/bin/env python

from CORDIAL.architectures.mlp import MLP
from CORDIAL.architectures.cordial import CORDIAL

class ModelFactory:
    """Factory for creating machine learning models by alias."""
    model_aliases = {
        'mlp': MLP,
        'cordial': CORDIAL
    }

    @classmethod
    def create_model(cls, alias, **kwargs):
        """
        Create model instance by alias.

        Args:
            alias: Model alias ('mlp' or 'cordial')
            **kwargs: Model-specific arguments

        Returns:
            Model instance

        Raises:
            ValueError: If alias is not recognized
        """
        model_class = cls.model_aliases.get(alias, None)
        if model_class:
            return model_class(**kwargs)
        else:
            raise ValueError(f"Unknown model alias: {alias}")
