from src.main import add
def test_add_success():
   assert add(1, 2, 3) == 6
   assert add(1.5, 2.5, 3) == 7.0
   assert add(0, 0, 0) == 0
   assert add(10, 10, 10) == 30
def test_add_type_error():
   assert add("1", 2, 3) == -1
   assert add(1, "2", 3) == -1
   assert add(1, 2, "3") == -1
   assert add(None, 2, 3) == -1
def test_add_range_error():
   assert add(-1, 2, 3) == -2
   assert add(11, 2, 3) == -2
   assert add(1, -1, 3) == -2
   assert add(1, 11, 3) == -2
   assert add(1, 2, -1) == -2
   assert add(1, 2, 11) == -2
