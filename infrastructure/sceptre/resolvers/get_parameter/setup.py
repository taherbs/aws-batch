from setuptools import setup

setup(
    name='get_parameter',
    py_modules=['get_parameter'],
    entry_points={
        'sceptre.resolvers': [
            'get_parameter = get_parameter:GetParameter',
        ],
    }
)
