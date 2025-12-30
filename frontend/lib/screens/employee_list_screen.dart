import 'package:flutter/material.dart';
import '../models/employee.dart';
import '../services/api_service.dart';

class EmployeeListScreen extends StatefulWidget {
  const EmployeeListScreen({super.key});

  @override
  State<EmployeeListScreen> createState() => _EmployeeListScreenState();
}

class _EmployeeListScreenState extends State<EmployeeListScreen> {
  late Future<List<Employee>> employees;

  @override
  void initState() {
    super.initState();
    employees = ApiService.fetchEmployees();
  }

  void refresh() {
    setState(() {
      employees = ApiService.fetchEmployees();
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Employees"),
        centerTitle: true,
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () => showEmployeeDialog(context),
        child: const Icon(Icons.add),
      ),
      body: FutureBuilder<List<Employee>>(
        future: employees,
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting) {
            return const Center(child: CircularProgressIndicator());
          }

          if (!snapshot.hasData || snapshot.data!.isEmpty) {
            return const Center(child: Text("No employees found"));
          }

          return ListView.builder(
            padding: const EdgeInsets.all(12),
            itemCount: snapshot.data!.length,
            itemBuilder: (context, index) {
              final emp = snapshot.data![index];
              return Card(
                elevation: 4,
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(16),
                ),
                child: ListTile(
                  title: Text(emp.name,
                      style: const TextStyle(fontWeight: FontWeight.bold)),
                  subtitle: Text(emp.address),
                  trailing: Row(
                    mainAxisSize: MainAxisSize.min,
                    children: [
                      IconButton(
                        icon: const Icon(Icons.edit),
                        onPressed: () =>
                            showEmployeeDialog(context, employee: emp),
                      ),
                      IconButton(
                        icon: const Icon(Icons.delete, color: Colors.red),
                        onPressed: () async {
                          await ApiService.deleteEmployee(emp.id);
                          refresh();
                        },
                      ),
                    ],
                  ),
                ),
              );
            },
          );
        },
      ),
    );
  }

  void showEmployeeDialog(BuildContext context, {Employee? employee}) {
    final nameCtrl = TextEditingController(text: employee?.name);
    final addressCtrl = TextEditingController(text: employee?.address);
    final salaryCtrl =
        TextEditingController(text: employee?.salary.toString());
    final contractCtrl =
        TextEditingController(text: employee?.contractyears.toString());
    final contactCtrl =
        TextEditingController(text: employee?.contact.toString());

    showDialog(
      context: context,
      builder: (_) => AlertDialog(
        title: Text(employee == null ? "Add Employee" : "Update Employee"),
        content: SingleChildScrollView(
          child: Column(
            children: [
              TextField(controller: nameCtrl, decoration: const InputDecoration(labelText: "Name")),
              TextField(controller: addressCtrl, decoration: const InputDecoration(labelText: "Address")),
              TextField(controller: salaryCtrl, decoration: const InputDecoration(labelText: "Salary"), keyboardType: TextInputType.number),
              TextField(controller: contractCtrl, decoration: const InputDecoration(labelText: "Contract Years"), keyboardType: TextInputType.number),
              TextField(controller: contactCtrl, decoration: const InputDecoration(labelText: "Contact"), keyboardType: TextInputType.number),
            ],
          ),
        ),
        actions: [
          TextButton(onPressed: () => Navigator.pop(context), child: const Text("Cancel")),
          ElevatedButton(
            onPressed: () async {
              final emp = Employee(
                id: employee?.id ?? 0,
                name: nameCtrl.text,
                address: addressCtrl.text,
                salary: double.parse(salaryCtrl.text),
                contractyears: int.parse(contractCtrl.text),
                contact: int.parse(contactCtrl.text),
              );

              if (employee == null) {
                await ApiService.addEmployee(emp);
              } else {
                await ApiService.updateEmployee(emp.id, emp);
              }

              // ignore: use_build_context_synchronously
              Navigator.pop(context);
              refresh();
            },
            child: const Text("Save"),
          )
        ],
      ),
    );
  }
}
