import mock
import types

import pytest

from jenkinsapi.result_set import ResultSet
from jenkinsapi.result import Result


class TestResultSet:

    DATA = {
        'duration': 0.0,
        'failCount': 2,
        'passCount': 0,
        'skipCount': 0,
        'suites': [{
            'cases': [{
                'age': 1,
                'className': '<nose.suite.ContextSuite context=jenkinsapi_tests',  # noqa
                'duration': 0.0,
                'errorDetails': 'Timeout error occured while waiting for Jenkins start.',  # noqa«
                'errorStackTrace': 'Traceback (most recent call last):\n  File "/usr/lib/python2.7/dist-packages/nose/suite.py", line 208, in run\n    self.setUp()\n  File "/usr/lib/python2.7/dist-packages/nose/suite.py", line 291, in setUp\n    self.setupContext(ancestor)\n  File "/usr/lib/python2.7/dist-packages/nose/suite.py", line 314, in setupContext\n    try_run(context, names)\n  File "/usr/lib/python2.7/dist-packages/nose/util.py", line 478, in try_run\n    return func()\n  File "/var/lib/jenkins/jobs/test_jenkinsapi/workspace/jenkinsapi/src/jenkinsapi_tests/systests/__init__.py", line 54, in setUpPackage\n    launcher = JenkinsLauncher(update_war=True, launch=True)\n  File "/var/lib/jenkins/jobs/test_jenkinsapi/workspace/jenkinsapi/src/jenkinsapi_tests/systests/__init__.py", line 20, in __init__\n    self.launch()\n  File "/var/lib/jenkins/jobs/test_jenkinsapi/workspace/jenkinsapi/src/jenkinsapi_tests/systests/__init__.py", line 41, in launch\n    raise Timeout(\'Timeout error occured while waiting for Jenkins start.\')\nTimeout: Timeout error occured while waiting for Jenkins start.\n',  # noqa
                'failedSince': 88,
                'name': 'systests>:setup',
                'skipped': False,
                'status': 'FAILED',
                'stderr': None,
                'stdout': None
            },
            {
                'age': 1,
                'className': 'nose.failure.Failure',
                'duration': 0.0,
                'errorDetails': 'No module named mock',
                'errorStackTrace': 'Traceback (most recent call last):\n  File "/usr/lib/python2.7/unittest/case.py", line 332, in run\n    testMethod()\n  File "/usr/lib/python2.7/dist-packages/nose/loader.py", line 390, in loadTestsFromName\n    addr.filename, addr.module)\n  File "/usr/lib/python2.7/dist-packages/nose/importer.py", line 39, in importFromPath\n    return self.importFromDir(dir_path, fqname)\n  File "/usr/lib/python2.7/dist-packages/nose/importer.py", line 86, in importFromDir\n    mod = load_module(part_fqname, fh, filename, desc)\n  File "/var/lib/jenkins/jobs/test_jenkinsapi/workspace/jenkinsapi/src/jenkinsapi_tests/unittests/test_build.py", line 1, in <module>\n    import mock\nImportError: No module named mock\n',  # noqa
                'failedSince': 88,
                'name': 'runTest',
                'skipped': False,
                'status': 'FAILED',
                'stderr': None,
                'stdout': None
            }
        ],
        'duration': 0.0,
        'id': None,
        'name': 'nosetests',
        'stderr': None,
        'stdout': None,
        'timestamp': None
    }],
    'childReports': [{
        "child": {
            "number": 1915,
            "url": "url1"
        },
        "result": None
    }]
    }

    @mock.patch.object(ResultSet, '_poll')
    @pytest.fixture
    def result_set(self, _poll):
        _poll.return_value = self.DATA
        build = mock.MagicMock()
        build.__str__.return_value = 'FooBuild'
        result_set = ResultSet('http://', build)
        return result_set

    def test_returns_a_string_when_repr_is_called_on_an_instance(self, result_set):
        assert repr(result_set) == 'Test Result for FooBuild'

    def test_returns_name_when_set(self, result_set):
        assert result_set.name == 'Test Result for FooBuild'

    def test_returns_iteritems(self, result_set):
        result = result_set.iteritems()

        assert isinstance(result, types.GeneratorType)

    def test_build_components(self, result_set):
        assert result_set.items()

        for k, v in result_set.items():
            assert isinstance(k, str)
            assert isinstance(v, Result)
            assert isinstance(v.identifier(), str)

    def test_keys(self, result_set):
        assert isinstance(result_set.keys(), list)

