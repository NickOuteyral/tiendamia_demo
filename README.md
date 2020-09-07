# tiendamia_demo


###_Brief Overview_

This is a proof of concept of an Acceptance Testing model, taking advantage of the Gherkin
format. This allows for tests that can be read as plain english but it executes test code in
the background, so to speak. The Gherkin itself can be seen in the .feature files located in
the `tests/acceptance/features` directory. Each of the declarations seen here reference a piece
of code in the `tests/acceptance/features/steps` folder, which in turn make use of the page models
and locators found at `tests/acceptance/features/page_model` and `tests/acceptance/features/locators`
as necessary. Besides of the Gherkin syntax use, the test suite employs the page object model.

More information regarding the Gherkin library for python can be found at the repository https://github.com/behave/behave


###_Setting up_

This project makes use of a few dependencies, found at the requirements.txt file, which are recommended
to be installed with pip. If opened with PyCharm the dependencies should be installed automatically, as well as
the Gherkin plugin, which are required to successfully run the tests. There are also some Run/Debug Configurations 
that must be addressed. The settings can be modified at the tab Run-->Edit Configurations of PyCharm. These configs
should look something like this:



As shown in the image, 