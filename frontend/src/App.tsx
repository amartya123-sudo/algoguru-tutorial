import { useEffect, useRef, useState } from "react";

import {
  Streamlit,
  withStreamlitConnection,
  type ComponentProps,
} from "streamlit-component-lib";

import MonacoEditor from "./MonacoEditor";

function App(props: ComponentProps) {
  const args = props.args;

  const [code, setCode] = useState(args.value ?? "");

  const previousRequest = useRef(false);

  useEffect(() => {
    setCode(args.value ?? "");
  }, [args.value]);

  useEffect(() => {
    Streamlit.setFrameHeight();
  });

  useEffect(() => {
    const request = args.request_code === true;

    // Only respond when request_code changes from false -> true
    if (request && !previousRequest.current) {
      Streamlit.setComponentValue(code);
    }

    previousRequest.current = request;
  }, [args.request_code, code]);

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
