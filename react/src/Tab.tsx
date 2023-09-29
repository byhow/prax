import { useState } from "react";

type TabsProp = {
  defaultValue: string;
  items: {
    label: string;
    value: string;
    panel: string;
  }[];
};

export default function Tabs({ defaultValue, items }: TabsProp) {
  const [value, setValue] = useState(defaultValue ?? items[0].value);

  return (
    <div className="tabs">
      <div className="tabs-list">
        {items.map(({ label, value: itemValue }) => {
          const isActiveValue = itemValue === value;

          return (
            <button
              key={itemValue}
              type="button"
              className={[
                "tabs-list-item",
                isActiveValue && "tabs-list-item--active",
              ]
                .filter(Boolean)
                .join(" ")}
              onClick={() => {
                setValue(itemValue);
              }}
            >
              {label}
            </button>
          );
        })}
      </div>
      <div>
        {items.map(({ panel, value: itemValue }) => (
          <div key={itemValue} hidden={itemValue !== value}>
            {panel}
          </div>
        ))}
      </div>
    </div>
  );
}
