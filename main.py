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
	"""แสดงงานทั้งหมดจากตัวแปร global `tasks` (อ่านง่ายเป็นภาษาไทย)"""
	global tasks

	if not tasks:
		print("ไม่มีงานในรายการ")
		return

	print("\nรายการงานทั้งหมด:")
	for t in tasks:
		print("-" * 40)
		print(f"ID: {t.get('id')}")
		print(f"ชื่อเรื่อง: {t.get('title')}")
		print(f"รายละเอียด: {t.get('description') or '-'}")
		print(f"วันครบกำหนด: {t.get('due_date') or '-'}")
		print(f"สถานะ: {'เสร็จแล้ว' if t.get('completed') else 'ยังไม่เสร็จ'}")
	print("-" * 40)


def edit_task():
	"""แก้ไขข้อมูลงานโดยให้ผู้ใช้เลือกจากลำดับ (index)

	ผู้ใช้สามารถแก้ `title`, `description` และ `completed` ได้
	จะตรวจสอบลำดับที่ป้อนมาว่าถูกต้องหรือไม่ (1..len(tasks))
	"""
	global tasks

	if not tasks:
		print("ไม่มีงานในรายการ")
		return

	print("\nเลือกงานที่ต้องการแก้ไข (ป้อนลำดับ)")
	for idx, t in enumerate(tasks, start=1):
		print(f"{idx}. {t.get('title')} (ID:{t.get('id')}) - {'เสร็จแล้ว' if t.get('completed') else 'ยังไม่เสร็จ'}")

	choice = input("ป้อนลำดับงาน (หมายเลข): ").strip()
	if not choice.isdigit():
		print("ลำดับไม่ถูกต้อง ต้องเป็นตัวเลข")
		return

	index = int(choice)
	if index < 1 or index > len(tasks):
		print("ลำดับไม่ถูกต้อง (อยู่นอกช่วง)")
		return

	task = tasks[index - 1]
	print(f"แก้ไขงาน ID={task.get('id')}, ชื่อเรื่องปัจจุบัน: {task.get('title')}")

	new_title = input("ชื่อเรื่องใหม่ (กด Enter เพื่อไม่เปลี่ยน): ").strip()
	if new_title:
		task['title'] = new_title

	new_description = input("รายละเอียดใหม่ (กด Enter เพื่อไม่เปลี่ยน): ").strip()
	if new_description:
		task['description'] = new_description

	new_completed = input("สถานะเสร็จแล้ว? (y = เสร็จ / n = ยังไม่เสร็จ, กด Enter เพื่อไม่เปลี่ยน): ").strip().lower()
	if new_completed in ('y', 'n'):
		task['completed'] = (new_completed == 'y')

	print("บันทึกการแก้ไขเรียบร้อย")


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
