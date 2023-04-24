import setuptools

# with open("README.md", "r", encoding="utf-8") as fh:
#     long_description = fh.read()

setuptools.setup(
    name='jenova_bot',
    version='0.0.1',
    author='John Eicher',
    author_email='john.eicher89@gmail.com',
    description='A basic bot in Discord',
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    url='https://github.com/saltchicken/jenova_bot',
    # project_urls = {
    #     "Bug Tracker": "https://github.com/saltchicken/jenova_bot/issues"
    # },
    # license='MIT',
    py_modules=['jenova_bot'],
    install_requires=['discord', 'pytube', 'moviepy'],
)
