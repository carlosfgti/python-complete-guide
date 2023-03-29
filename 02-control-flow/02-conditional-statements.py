total_courses = 90
goal = 70
next_goal = 80

if total_courses > next_goal:
  print("Nada a fazer, você superou tudo")
elif total_courses > goal:
  print("Parabéns, meta atingida")
  print(f"Próxima meta: {next_goal}")
else:
  print("Ops, meta ainda não foi atingida")
  print(f"faltam {goal - total_courses} cursos para atingir a meta")

print("-- end --")