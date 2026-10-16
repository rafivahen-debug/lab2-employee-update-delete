from flask import Blueprint, jsonify, request, render_template, redirect, url_for, flash
from models.employee_model import employees

employee_bp = Blueprint("employee_bp", __name__)

@employee_bp.route("/employees", methods=["GET"])
def list_employees():
    return jsonify(employees), 200

@employee_bp.route("/employees/<int:id>", methods=["GET"])
def get_employee(id):
    employee = next((e for e in employees if e["id"] == id), None)
    if employee is None:
        return jsonify({"error": "Employee tidak ditemukan"}), 404
    return jsonify(employee), 200

@employee_bp.route("/employees/new", methods=["GET", "POST"])
def show_form():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        position = request.form.get("position", "Staff").strip() or "Staff"
        salary_raw = request.form.get("salary", "0").strip()
        if not name:
            flash("Nama employee wajib diisi.", "error")
            return redirect(url_for("employee_bp.show_form"))
        try:
            salary = int(salary_raw or 0)
            if salary < 0:
                raise ValueError
        except ValueError:
            flash("Gaji harus berupa angka nol atau lebih.", "error")
            return redirect(url_for("employee_bp.show_form"))
        new_id = max((e["id"] for e in employees), default=0) + 1
        employees.append({"id": new_id, "name": name, "position": position, "salary": salary})
        flash("Employee berhasil ditambahkan.", "success")
        return redirect(url_for("employee_bp.show_form"))
    return render_template("form.html", employees=employees)

@employee_bp.route("/employees/<int:id>/edit", methods=["GET", "POST"])
def edit_employee(id):
    employee = next((e for e in employees if e["id"] == id), None)
    if employee is None:
        return "Employee tidak ditemukan", 404
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        position = request.form.get("position", "Staff").strip() or "Staff"
        salary_raw = request.form.get("salary", "0").strip()
        if not name:
            flash("Nama employee wajib diisi.", "error")
            return redirect(url_for("employee_bp.edit_employee", id=id))
        try:
            salary = int(salary_raw or 0)
            if salary < 0:
                raise ValueError
        except ValueError:
            flash("Gaji harus berupa angka nol atau lebih.", "error")
            return redirect(url_for("employee_bp.edit_employee", id=id))
        employee.update({"name": name, "position": position, "salary": salary})
        flash("Data employee berhasil diperbarui.", "success")
        return redirect(url_for("employee_bp.show_form"))
    return render_template("form.html", employees=employees, edit_employee=employee)

@employee_bp.route("/employees/<int:id>/delete", methods=["POST"])
def delete_employee(id):
    employee = next((e for e in employees if e["id"] == id), None)
    if employee is None:
        flash("Employee tidak ditemukan.", "error")
    else:
        employees.remove(employee)
        flash("Employee berhasil dihapus.", "success")
    return redirect(url_for("employee_bp.show_form"))
