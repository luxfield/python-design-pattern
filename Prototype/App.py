from Store import Store
store1 = Store("toko x", "jakarta", "indonesia", "gadget")
print(store1.get_name())
store2 = store1.clone()
store2.set_name("toko Y")
print(store2.get_name())
