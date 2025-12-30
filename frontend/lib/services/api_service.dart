import 'dart:convert';
import 'package:http/http.dart' as http;
import '../models/employee.dart';

class ApiService {
  static const String baseUrl = "http://192.168.18.13:8000";

  static Future<List<Employee>> fetchEmployees() async {
    final response = await http.get(Uri.parse("$baseUrl/"));
    final List data = json.decode(response.body);
    return data.map((e) => Employee.fromJson(e)).toList();
  }

  static Future<void> addEmployee(Employee employee) async {
    await http.post(
      Uri.parse("$baseUrl/"),
      headers: {"Content-Type": "application/json"},
      body: jsonEncode(employee.toJson()),
    );
  }

  static Future<void> updateEmployee(int id, Employee employee) async {
    await http.put(
      Uri.parse("$baseUrl/?id=$id"),
      headers: {"Content-Type": "application/json"},
      body: jsonEncode(employee.toJson()),
    );
  }

  static Future<void> deleteEmployee(int id) async {
    await http.delete(Uri.parse("$baseUrl/?id=$id"));
  }
}
