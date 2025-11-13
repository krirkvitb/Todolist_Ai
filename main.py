tasks = []


def add_task():
	"""รับข้อมูลงานใหม่จากผู้ใช้และเพิ่มลงในตัวแปร global `tasks`.

	โครงสร้างงาน: dict มี key: id, title, description, due_date, completed
	"""
	global tasks

	# หา id ถัดไป (incremental)
	if tasks:
		try:
			next_id = max(t.get('id', 0) for t in tasks) + 1
		except Exception:
			next_id = 1
	else:
		next_id = 1

	# รับข้อมูลจากผู้ใช้
	while True:
		title = input("ชื่อเรื่อง: ").strip()
		if title:
			break
		print("ชื่อเรื่องห้ามว่าง กรุณากรอกใหม่")

	description = input("รายละเอียด: ").strip()
	due_date = input("วันครบกำหนด (YYYY-MM-DD หรือข้อความ): ").strip()

	task = {
		'id': next_id,
		'title': title,
		'description': description,
		'due_date': due_date,
		'completed': False,
	}

	tasks.append(task)
	print(f"เพิ่มงานเรียบร้อย (id={next_id})")


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
