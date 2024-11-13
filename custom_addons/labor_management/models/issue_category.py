from odoo import api, fields, models, _, tools

class IssueCategory(models.Model):
    _name = "labor.issue.category"
    _description = "Labor Issue Category"

    name = fields.Char(string="Category Name", required=True)
    description = fields.Text(string="Category Description")
    issue_count = fields.Integer(string="Issue Count", compute="_compute_issue_count", store=True)
    labor_issue_ids = fields.One2many('labor.issues', 'category_id', string="Issues")

    @api.depends('labor_issue_ids')
    def _compute_issue_count(self):
        for category in self:
            category.issue_count = len(category.labor_issue_ids)

    @api.model
    def get_most_needed_category(self):
        most_needed_category = self.search([], order='issue_count desc', limit=1)
        return most_needed_category