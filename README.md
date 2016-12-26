# rhi-pool
Tests for different components in Red Hat Insights

### Setup
```
pip install -r requirements.txt

mv pool.conf.sample pool.conf
#Make appropriate changes to pool.conf
```

### Execution
```
#Running the UI tests
py.test -s -v tests/portal

#Running the api tests
py.test -s -v tests/api

#Running the tests against Satellite 6
py.test -s -v tests/satellite6

#Running a single test eg. test_register_machine_sat6
py.test -s -v tests/satellite6/test_sat6_register.py::Satellite6APITestCase::test_register_machine_sat6
```

