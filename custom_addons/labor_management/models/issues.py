from odoo import api, fields, models, _, tools

class laborIssues(models.Model):
    _name = "labor.issues"

    description = fields.Char(string="Issue Description")
    location = fields.Char(string="Location")
    status = fields.Selection([
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved')
    ], string="Status", default='new')
    assigned_to = fields.Many2one(comodel_name='labor.employee', string='Assigned To')
    category_id = fields.Many2one(comodel_name='labor.issue.category', string="Category")
    issue_count = fields.Integer(string="Issue Count", compute="_compute_issue_count", store=True)
    labor_issue_ids = fields.One2many('labor.issues', 'category_id', string="Issues")


    @api.model
    def create(self, description, issue_type, location, status, assigned_to_id, category_id):
        new_issue = self.create({
            'description': description,
            'issue_type': issue_type,
            'location': location,
            'status': status,
            'assigned_to': assigned_to_id,
            'category_id': category_id,
        })
        return new_issue


    @api.depends('labor_issue_ids')
    def _compute_issue_count(self):
        for category in self:
            category.issue_count = len(category.labor_issue_ids)

    @api.model
    def get_most_needed_category(self):
        most_needed_category = self.search([], order='issue_count desc', limit=1)
        return most_needed_category