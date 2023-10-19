import { useEffect, useState } from "react";
import "./stoplight.css";
type StopLightState = "stop" | "slow" | "go";

const STOP_DELAY = 3000;
const SLOW_DELAY = 2000;
const GO_DELAY = 5000;

function TrafficLight() {
  const [state, setState] = useState<StopLightState>("stop");

  function getStopLightClass(light: StopLightState) {
    return `light ${light}` + (state === light ? " on" : "");
  }

  useEffect(() => {
    if (state === "stop") {
      setTimeout(() => setState("go"), GO_DELAY);
    } else if (state === "slow") {
      setTimeout(() => setState("stop"), STOP_DELAY);
    } else {
      setTimeout(() => setState("slow"), SLOW_DELAY);
    }
  }, [state]);

  return (
    <div className="stop-light">
      <div className={getStopLightClass("stop")}></div>
      <div className={getStopLightClass("slow")}></div>
      <div className={getStopLightClass("go")}></div>
    </div>
  );
}

export default TrafficLight;
