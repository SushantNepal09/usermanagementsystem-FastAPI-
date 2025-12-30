class Employee {
  final int id;
  final String name;
  final String address;
  final double salary;
  final int contractyears;
  final int contact;

  Employee({
    required this.id,
    required this.name,
    required this.address,
    required this.salary,
    required this.contractyears,
    required this.contact,
  });

  factory Employee.fromJson(Map<String, dynamic> json) {
    return Employee(
      id: json['id'],
      name: json['name'],
      address: json['address'],
      salary: (json['salary'] as num).toDouble(),
      contractyears: json['contractyears'],
      contact: json['contact'],
    );
  }

  Map<String, dynamic> toJson() {
    return {
      "id": id,
      "name": name,
      "address": address,
      "salary": salary,
      "contractyears": contractyears,
      "contact": contact,
    };
  }
}
