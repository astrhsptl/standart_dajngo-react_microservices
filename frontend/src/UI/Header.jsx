import React from 'react'
import { Link } from 'react-router-dom'
import paths from '../utils/paths'


export default function Header(props) {
  return (
    <div className={'header'}>
        {paths.map(route => (
            (props.path !== route.path) ? <Link key={route.path} to={route.path}> {route.name}</Link> : console.log()
        ))}
    </div>
  )
}
