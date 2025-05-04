import logging
from dataclasses import dataclass, field
from typing import Optional

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

VALID_STATUSES = ["PENDING", "PROCESSING", "SHIPPED", "DELIVERED", "CANCELLED"]

@dataclass
class Order:
    order_id: str
    status: str = "PENDING"
    tracking_number: Optional[str] = None
    items: list = field(default_factory=list)

    def __post_init__(self):
        if self.status not in VALID_STATUSES:
            raise ValueError(f"Invalid initial status: {self.status}")

def set_tracking_number(order: Order, tracking: str):
    """Sets the tracking number, only if the order is SHIPPED."""
    if order.status == "SHIPPED":
        order.tracking_number = tracking
        logging.info(f"Order {order.order_id}: Tracking number set to {tracking}")
    else:
        logging.warning(f"Order {order.order_id}: Cannot set tracking number in status {order.status}")

# --- Flawed Implementation ---
def advance_order_status(order: Order) -> bool:
    """
    Advances the order to the next logical status.
    (Flaw: Missing validation for tracking number before DELIVERED state).
    """
    current_status = order.status
    next_status = None
    success = False

    if current_status == "PENDING":
        next_status = "PROCESSING"
    elif current_status == "PROCESSING":
        next_status = "SHIPPED"
    elif current_status == "SHIPPED":
        # Flaw: Should check if order.tracking_number is set BEFORE advancing!
        # The issue requires this check, but the code forgets it.
        next_status = "DELIVERED"
    elif current_status in ["DELIVERED", "CANCELLED"]:
        logging.warning(f"Order {order.order_id}: Cannot advance status from {current_status}")
        return False

    if next_status:
        order.status = next_status
        logging.info(f"Order {order.order_id}: Status advanced from {current_status} to {next_status}")
        success = True
    else:
        # Should not happen with current logic, but good practice
        logging.error(f"Order {order.order_id}: Could not determine next status from {current_status}")
        success = False

    return success

# --- Example Usage ---
if __name__ == "__main__":
    order1 = Order(order_id="ORD123", items=["item1", "item2"])
    print(f"Initial state: {order1}")

    advance_order_status(order1) # PENDING -> PROCESSING
    print(f"State after 1st advance: {order1}")

    advance_order_status(order1) # PROCESSING -> SHIPPED
    print(f"State after 2nd advance: {order1}")

    # Attempt to advance without setting tracking number (SHOULD ideally fail based on intent)
    print("\nAttempting to advance SHIPPED order without tracking number...")
    advance_order_status(order1) # SHIPPED -> DELIVERED (Flaw allows this)
    print(f"State after 3rd advance (no tracking): {order1}") # Shows DELIVERED

    # Reset and try again, setting tracking number this time
    order2 = Order(order_id="ORD456", items=["item3"])
    advance_order_status(order2) # PENDING -> PROCESSING
    advance_order_status(order2) # PROCESSING -> SHIPPED
    set_tracking_number(order2, "TRK98765") # Set tracking number correctly
    print(f"\nOrder 2 state before final advance: {order2}")
    print("Attempting to advance SHIPPED order with tracking number...")
    advance_order_status(order2) # SHIPPED -> DELIVERED (Works as expected here)
    print(f"State after final advance (with tracking): {order2}")

    # Try advancing a delivered order
    print("\nAttempting to advance a DELIVERED order...")
    advance_order_status(order2) # Should log warning and return False
    print(f"State after trying to advance DELIVERED: {order2}")
