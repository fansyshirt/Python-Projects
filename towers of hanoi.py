def towers_of_hanoi(number_of_disks, start_peg, spare_peg, target_peg):
  if number_of_disks == 1:
    print(f"Move disk 1 from {start_peg} to {target_peg}")
    return
  towers_of_hanoi(number_of_disks - 1, start_peg, target_peg, spare_peg)
  print(f"Move disk {number_of_disks} from {start_peg} to {target_peg}")
  towers_of_hanoi(number_of_disks - 1, spare_peg, start_peg, target_peg)
num_disks = int(input("Enter the number of disks: "))
towers_of_hanoi(num_disks, 'Peg A', 'Peg B', 'Peg C')
