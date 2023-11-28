# -*- coding: utf-8 -*-

from odoo import models, fields, api


class escuela(models.Model):
    _name = "escuela.profesor"
    _description = "escuela"

    name = fields.Char(string="name", required=True)
    age = fields.Integer(string="age", required=True)   
    born = fields.Date(string="Born age", required=True) 
    salary = fields.Float(string="Salary", required=True)
    status = fields.Boolean(string="Status", required=True)
    grade = fields.Selection(
        [
        ("primary", "Primary"),
        ("segundary","Segundary"),
        ],
        string="Grade",
        default="primary",
        require=True,
    )
    student = fields.One2many("escuela.student",inverse_name="teacher",string="student")

    subjects  = fields.Many2many(

        comodel_name="escuela.subjects",
        relation_name="escuela_subjects",
        column1="escuela_id",
        column2="subjects_id",
    )

class student(models.Model):
    _name = "escuela.student"
    _description = "escuela"

    name = fields.Char(string="name", required=True)
    age = fields.Integer(string="age", required=True)   
    teacher = fields.Many2one("escuela.profesor",string="teacher", required=True)
    grade_id = fields.One2many("escuela.grade", "student_id",string="grade")

class subjects(models.Model):
    _name = "escuela.subjects"
    _description = "subjects"
    
    name = fields.Char(string="Subjects", required=True)
    credit = fields.Integer(string="Credit")
    teacher  = fields.Many2many(
        comodel_name="escuela.profesor",
        relation_name="escuela_subjects",
        column1="subjects_id",
        column2="escuela_id",  
    )

class grade(models.Model):
    _name = "escuela.grade"
    _description = "grade"
    student_id = fields.Many2one("escuela.student", string="Student")
    subject_id = fields.Many2one("escuela.subjects", string="subjects")
    grade = fields.Integer(string="Grade",required=True)
    status = fields.Char("Status",compute="_compute_status")
    @api.depends("grade")
    def _compute_status(self):
        for record in self:
            if record.grade >= 70:
                record.status = "aproved"
            else:
                record.status = "reprove"

    