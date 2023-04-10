"""AddIsAdminUsersTable Migration."""

from masoniteorm.migrations import Migration


class AddIsAdminUsersTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table("users") as table:
            table.boolean('is_admin').default(False)

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table("users") as table:
            pass
