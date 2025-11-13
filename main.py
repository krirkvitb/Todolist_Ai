def add_task():
	"""Placeholder: เพิ่มงานใหม่ (ยังไม่ได้ implement)"""
	pass


def view_tasks():
	"""Placeholder: ดูงานทั้งหมด (ยังไม่ได้ implement)"""
	pass


def edit_task():
	"""Placeholder: แก้ไขงาน (ยังไม่ได้ implement)"""
	pass


def delete_task():
	"""Placeholder: ลบงาน (ยังไม่ได้ implement)"""
	pass


def exit_program():
	"""Placeholder: ออกจากโปรแกรม (ยังไม่ได้ implement)"""
	pass


def main():
	while True:
		print("\nTodolist - เมนูหลัก")
		print("1. เพิ่มงานใหม่")
		print("2. ดูงานทั้งหมด")
		print("3. แก้ไขงาน")
		print("4. ลบงาน")
		print("5. ออกจากโปรแกรม")
		choice = input("เลือกตัวเลือก (1-5): ").strip()

		if choice == '1':
			add_task()
		elif choice == '2':
			view_tasks()
		elif choice == '3':
			edit_task()
		elif choice == '4':
			delete_task()
		elif choice == '5':
			exit_program()
			print("ออกจากโปรแกรม")
			break
		else:
			print("ตัวเลือกไม่ถูกต้อง กรุณาลองใหม่")


if __name__ == "__main__":
	main()
