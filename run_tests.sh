ag -l | entr -s 'echo "BEGIN TESTS"; nosetests tests; echo "FINISHED TESTS"' 
