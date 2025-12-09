import logging

import pandas as pd
import pandas_checks as pdc

from .method_chains import flatten_columns, assign_with_apply

# Logging
logger = logging.getLogger(__name__)
format = "[%(asctime)s] %(levelname)s | %(message)s "
logging.basicConfig(level=logging.DEBUG, format=format)

# Pandas checks
pdc.set_custom_print_fn(logger.info, print_to_stdout=False)
pdc.set_format(precision=3, use_emojis=False)
