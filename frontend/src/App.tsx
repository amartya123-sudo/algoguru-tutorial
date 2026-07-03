import { useEffect, useState, useRef } from "react";

import { Streamlit, withStreamlitConnection } from "streamlit-component-lib";

import type { ComponentProps } from "streamlit-component-lib";

import MonacoEditor from "./MonacoEditor";

function App(props: ComponentProps) {
  const args = props.args;

  const [code, setCode] = useState(args.value ?? "");

  const pendingRequest = useRef(false);

  useEffect(() => {
    setCode(args.value ?? "");
  }, [args.value]);

  // Python tells component: "send me current code now"
  useEffect(() => {
    if (args.request_code === true && pendingRequest.current === false) {
      pendingRequest.current = true;

      Streamlit.setComponentValue({
        code,
      });

      setTimeout(() => {
        pendingRequest.current = false;
      }, 0);
    }
  }, [args.request_code]);

  useEffect(() => {
    Streamlit.setFrameHeight();
  });

  return (
    <MonacoEditor
      value={code}
      language={args.language ?? "python"}
      theme={args.theme ?? "vs-dark"}
      height={args.height ?? 500}
      onChange={(value) => {
        setCode(value ?? "");
      }}
    />
  );
}

export default withStreamlitConnection(App);
