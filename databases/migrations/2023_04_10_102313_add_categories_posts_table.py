"""AddCategoriesPostsTable Migration."""

from masoniteorm.migrations import Migration


class AddCategoriesPostsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table("posts") as table:
            table.integer('categories_id').unsigned()
            table.foreign('categories_id').references('id').on('categories')

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table("posts") as table:
            pass
