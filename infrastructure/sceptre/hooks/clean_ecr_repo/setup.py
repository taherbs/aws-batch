from setuptools import setup

setup(
    name='clean_ecr_repo',
    py_modules=['clean_ecr_repo'],
    entry_points={
        'sceptre.hooks': [
            'clean_ecr_repo = clean_ecr_repo:CleanEcrRepo',
        ],
    }
)
