"""ChangeBody Migration."""

from masoniteorm.migrations import Migration


class ChangeBody(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table("posts") as table:
            table.text('body').nullable()


    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table("posts") as table:
            table.drop_column('body')
            
