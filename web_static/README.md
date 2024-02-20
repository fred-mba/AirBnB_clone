## AirBnB clone - Web static

- The `display: flex;` property in CSS is used to define a flex container. When you apply `display: flex;` to an element, it becomes a flex container, and its direct children become flex items.

Characteristics a flex container:

1. Flex Container (Parent):

- The element with `display: flex;` becomes a flex container.
- The child elements of this container become flex items.
2. Flex Items:

- Elements that are direct children of a flex container are automatically treated as flex items.
- Flex items can be horizontally or vertically aligned, reordered, and resized within the flex container.

3. Flex Direction:
- By default, the main axis of the flex container is horizontal (left to right). However, you can use the flex-direction property to change it to vertical (top to bottom) if needed.

4. Flex Wrapping:
- By default, flex items will try to fit in a single line. If there's not enough space, they will shrink. You can use the flex-wrap property to allow flex items to wrap onto multiple lines.

5. Aligning Items:
- The `align-items` property is used to align flex items vertically along the cross-axis (perpendicular to the main axis).
- The justify-content property is used to align flex items along the main axis.

6. Ordering Items:
- The `order` property allows you to change the order of flex items. By default, all items have an order of 0, but you can set a positive or negative value to reorder them.