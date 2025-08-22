import React, { useEffect, useRef, memo } from 'react';

function TradingViewWidget() {
  const container = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const containerEl = container.current;
    if (!containerEl) return;

    containerEl.innerHTML = '';
    const script = document.createElement('script');
    script.type = 'text/javascript';
    script.async = true;
    script.crossOrigin = 'anonymous';
    script.src = 'https://s3.tradingview.com/external-embedding/embed-widget-advanced-chart.js';
    script.onerror = (e) => {
      console.error('TradingView widget failed to load', e);
    };
    script.innerHTML = `{
      "allow_symbol_change": true,
      "calendar": false,
      "details": false,
      "hide_side_toolbar": true,
      "hide_top_toolbar": false,
      "hide_legend": false,
      "hide_volume": false,
      "hotlist": false,
      "interval": "1",
      "locale": "br",
      "save_image": true,
      "style": "1",
      "symbol": "OANDA:EURUSD",
      "theme": "dark",
      "timezone": "Etc/UTC",
      "backgroundColor": "#0F0F0F",
      "gridColor": "rgba(242, 242, 242, 0.06)",
      "watchlist": [],
      "withdateranges": false,
      "compareSymbols": [],
      "studies": [],
      "autosize": true
    }`;
    containerEl.appendChild(script);

    return () => {
      containerEl.innerHTML = '';
    };
  }, []);

  useEffect(() => {
    const handleWindowError = (event: ErrorEvent) => {
      if (event.message === 'Script error.' && event.filename === '') {
        console.error('Cross-origin script error', event);
        event.preventDefault();
      }
    };

    window.addEventListener('error', handleWindowError);
    return () => {
      window.removeEventListener('error', handleWindowError);
    };

  }, []);

  return (
    <div
      className="tradingview-widget-container"
      ref={container}
      style={{ height: '100%', width: '100%' }}
    >
      <div
        className="tradingview-widget-container__widget"
        style={{ height: 'calc(100% - 32px)', width: '100%' }}
      ></div>
      <div className="tradingview-widget-copyright">
        <a
          href="https://br.tradingview.com/symbols/OANDA-EURUSD/?exchange=OANDA"
          rel="noopener nofollow"
          target="_blank"
        >
          <span className="blue-text">Track all markets on TradingView</span>
        </a>
      </div>
    </div>
  );
}

export default memo(TradingViewWidget);

