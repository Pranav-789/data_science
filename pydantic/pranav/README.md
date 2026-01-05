# **Pydantic Learning Project**

This project documents a comprehensive learning journey through **Pydantic**, organized into structured modules with examples and assignments. It includes core concepts, advanced patterns, and integration with **FastAPI**.

---

## **Project Setup**

This project was organized in a structured directory (`pranav`) to keep examples, assignments, and exercises separate.

### Requirements

* Python >= 3.13
* **Dependencies**:

  * `pydantic` >= 2.12.5 — Core Pydantic library
  * `pydantic-settings` >= 2.12.0 — For managing application settings
  * `fastapi` >= 0.128.0 — Web framework
  * `uvicorn` >= 0.40.0 — ASGI server
  * `python-dotenv` >= 1.2.1 — Environment variable management

**Installation:**

```bash
uv sync
```

> Note: `uv` is used here for fast dependency management.

---

## **Project Structure**

### **Core Learning Modules (01–06)**

#### `01_foundation/`

* **Focus**: Pydantic basics — creating models, understanding type hints and default behaviors.
* **Examples**: Basic model creation and usage
* **Assignment**: Implement a `Product` model

#### `02_field_validation/`

* **Focus**: Field validation and constraints
* **Examples**: Validating strings, numbers, enums, and using Pydantic validators
* **Assignment**: Create an `Employee` model with field validation

#### `03_model_behaviour/`

* **Focus**: Model behavior, custom validators, computed fields, and model methods
* **Examples**: Custom validators, methods like `model.dict()` and `model.json()`
* **Assignment**: Implement a `Booking` model with custom validations

#### `04_nested_models/`

* **Focus**: Nested models, complex data structures, and lists of models
* **Examples**: Using `BaseModel` inside another model, nested validation
* **Assignment**: Design complex nested models

#### `05_serialization/`

* **Focus**: Serialization and deserialization of data
* **Examples**: Converting models to/from JSON, handling aliases and extra fields

#### `06_fast_api/`

* **Focus**: Integrating Pydantic models with **FastAPI** for REST APIs
* **Examples**: Path parameters, request bodies, response models, and validation

---

### **Bonus Module**

#### `07_dependency_injection/`

* **Focus**: Exploring dependency injection patterns in Python and FastAPI
* **Examples**: Using `Depends()` to inject services, settings, or database sessions

---

## **Learning Path**

The modules are designed to be followed sequentially:

1. Foundations → `01_foundation/`
2. Field validation & model behavior → `02_` – `03_`
3. Advanced patterns → `04_` – `05_`
4. FastAPI integration → `06_`
5. Bonus concepts (DI) → `07_`

---

## **How to Use**

1. Navigate through the modules in order.
2. Explore the `examples/` folder in each module for guided examples.
3. Complete the exercises in `assignments/` to reinforce learning.
4. Experiment by modifying models or creating new ones.