# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: AssetCheckout
TEMPLATE_REGISTRY = {}

def register_template(name, fields):
    """Register a checkout template with required fields."""
    TEMPLATE_REGISTRY[name] = fields

def create_from_template(template_name, recipient, template_fields):
    """Create a new checkout record based on a registered template."""
    if template_name not in TEMPLATE_REGISTRY:
        raise ValueError(f"Unknown template: {template_name}")
    required = TEMPLATE_REGISTRY[template_name]
    for field in required:
        if field not in template_fields:
            raise ValueError(f"Template '{template_name}' requires field: {field}")
    return {
        'recipient': recipient,
        'item': template_fields.get('item', 'Unknown'),
        'status': 'active',
        'date': datetime.now().strftime('%Y-%m-%d'),
        'template': template_name,
    }
