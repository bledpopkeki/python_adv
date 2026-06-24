import streamlit as st
import pandas as pd
import json
import os

# -----------------------------
# FILE PATHS
# -----------------------------
RECIPES_FILE = "recipes.json"
CATEGORIES_FILE = "categories.json"


# -----------------------------
# HELPER FUNCTIONS
# -----------------------------
def load_data(file_path, default_data):
    if not os.path.exists(file_path):
        with open(file_path, "w") as file:
            json.dump(default_data, file)

    with open(file_path, "r") as file:
        return json.load(file)


# -----------------------------
# RECIPE FUNCTIONS
# -----------------------------
def get_recipes():
    return load_data(RECIPES_FILE, [])


def save_recipes(recipes):
    with open(RECIPES_FILE, "w") as file:
        json.dump(recipes, file, indent=4)


def create_recipe(name, ingredients, instructions, category):
    recipes = get_recipes()

    recipe = {
        "name": name,
        "ingredients": ingredients,
        "instructions": instructions,
        "category": category
    }

    recipes.append(recipe)
    save_recipes(recipes)


def update_recipe(index, name, ingredients, instructions, category):
    recipes = get_recipes()

    recipes[index] = {
        "name": name,
        "ingredients": ingredients,
        "instructions": instructions,
        "category": category
    }

    save_recipes(recipes)


def delete_recipe(index):
    recipes = get_recipes()
    recipes.pop(index)
    save_recipes(recipes)


# -----------------------------
# CATEGORY FUNCTIONS
# -----------------------------
def get_categories():
    return load_data(CATEGORIES_FILE, [])


def save_categories(categories):
    with open(CATEGORIES_FILE, "w") as file:
        json.dump(categories, file, indent=4)


def create_category(category_name):
    categories = get_categories()

    if category_name not in categories:
        categories.append(category_name)
        save_categories(categories)


def delete_category(category_name):
    categories = get_categories()

    if category_name in categories:
        categories.remove(category_name)
        save_categories(categories)


# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Recipe Manager",
    page_icon="🍔",
    layout="wide"
)

st.title("🍔 Recipe Management System")


# -----------------------------
# SIDEBAR NAVIGATION
# -----------------------------
menu = st.sidebar.selectbox(
    "Navigation",
    [
        "Dashboard",
        "Manage Recipes",
        "Manage Categories"
    ]
)


# -----------------------------
# DASHBOARD
# -----------------------------
if menu == "Dashboard":

    st.header("📊 Dashboard")

    recipes = get_recipes()
    categories = get_categories()

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Recipes")

        if recipes:
            recipe_df = pd.DataFrame(recipes)
            st.dataframe(recipe_df)
        else:
            st.info("No recipes available.")

    with col2:
        st.subheader("Categories")

        if categories:
            category_df = pd.DataFrame(categories, columns=["Category"])
            st.dataframe(category_df)
        else:
            st.info("No categories available.")


# -----------------------------
# MANAGE RECIPES
# -----------------------------
elif menu == "Manage Recipes":

    st.header("🍳 Manage Recipes")

    categories = get_categories()
    recipes = get_recipes()

    # ADD RECIPE
    st.subheader("Add New Recipe")

    with st.form("recipe_form"):

        recipe_name = st.text_input("Recipe Name")

        ingredients = st.text_area(
            "Ingredients",
            placeholder="Enter ingredients..."
        )

        instructions = st.text_area(
            "Instructions",
            placeholder="Enter instructions..."
        )

        category = st.selectbox(
            "Category",
            categories
        )

        submit_recipe = st.form_submit_button("Add Recipe")

        if submit_recipe:
            create_recipe(
                recipe_name,
                ingredients,
                instructions,
                category
            )

            st.success("Recipe added successfully!")
            st.rerun()

    st.divider()

    # DISPLAY RECIPES
    st.subheader("Existing Recipes")

    if recipes:

        for index, recipe in enumerate(recipes):

            with st.expander(f"{recipe['name']} ({recipe['category']})"):

                st.write(f"**Ingredients:** {recipe['ingredients']}")
                st.write(f"**Instructions:** {recipe['instructions']}")

                col1, col2 = st.columns(2)

                with col1:
                    if st.button(
                        f"Delete {recipe['name']}",
                        key=f"delete_{index}"
                    ):
                        delete_recipe(index)
                        st.success("Recipe deleted!")
                        st.rerun()

                with col2:
                    with st.popover("Edit Recipe"):

                        new_name = st.text_input(
                            "New Name",
                            value=recipe['name'],
                            key=f"name_{index}"
                        )

                        new_ingredients = st.text_area(
                            "New Ingredients",
                            value=recipe['ingredients'],
                            key=f"ingredients_{index}"
                        )

                        new_instructions = st.text_area(
                            "New Instructions",
                            value=recipe['instructions'],
                            key=f"instructions_{index}"
                        )

                        new_category = st.selectbox(
                            "New Category",
                            categories,
                            index=categories.index(recipe['category']) if recipe['category'] in categories else 0,
                            key=f"category_{index}"
                        )

                        if st.button(
                            "Update Recipe",
                            key=f"update_{index}"
                        ):

                            update_recipe(
                                index,
                                new_name,
                                new_ingredients,
                                new_instructions,
                                new_category
                            )

                            st.success("Recipe updated!")
                            st.rerun()

    else:
        st.info("No recipes found.")


# -----------------------------
# MANAGE CATEGORIES
# -----------------------------
elif menu == "Manage Categories":

    st.header("📂 Manage Categories")

    categories = get_categories()

    st.subheader("Add New Category")

    new_category = st.text_input("Category Name")

    if st.button("Add Category"):

        if new_category.strip() != "":
            create_category(new_category)
            st.success("Category added!")
            st.rerun()

        else:
            st.error("Please enter a category name.")

    st.divider()

    st.subheader("Existing Categories")

    if categories:

        for category in categories:

            col1, col2 = st.columns([4, 1])

            with col1:
                st.write(category)

            with col2:
                if st.button(
                    "Delete",
                    key=f"delete_cat_{category}"
                ):
                    delete_category(category)
                    st.success("Category deleted!")
                    st.rerun()

    else: fast API CRUD
        st.info("No categories found.")