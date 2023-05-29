from odoo import api, fields, models, _
import logging
import psutil
import netifaces as ni
import socket

_logger = logging.getLogger(__name__)


class IrHttp(models.AbstractModel):
    _inherit = 'ir.http'

    def session_info(self):
        result = super(IrHttp, self).session_info()

        try:
            result['interval'] = self.env['res.config.settings'].search_read([], ['update_frequency'])[-1]['update_frequency']
        except Exception as ex:
            _logger.error(f" {ex}")
            result['interval'] = 5000

        result['cpu_usage'] = f'{psutil.cpu_percent()} %'
        result['cpu_count'] = psutil.cpu_count()

        mem_info = psutil.virtual_memory()
        result['mem_total'] = f'{(mem_info.total):.0f} GB'
        result['mem_used'] = f'{(mem_info.used):.0f} GB'
        result['mem_used_percent'] = f'{mem_info.percent} %'
        result['mem_free'] = f'{(mem_info.free/(1024*1024)):.0f} Mb'

        disk_mem_info = psutil.disk_usage('/')
        result['disk_mem_total'] = f'{(disk_mem_info.total ):.0f} GB'
        result['disk_mem_used'] = f'{(disk_mem_info.used ):.0f} GB'
        result['disk_mem_used_percent'] = f'{disk_mem_info.percent} %'
        result['disk_mem_free'] = f'{(disk_mem_info.free ):.0f} Mb'

        host_name = self.env['ir.config_parameter'].get_param('web.base.url')
        ip4_info = ni.ifaddresses('ens3')[ni.AF_INET][0]['addr']
        result['ip4_info'] = f'{(ip4_info)}'
        ip6_info = ni.ifaddresses('ens3')[ni.AF_INET6][0]['addr']
        result['ip6_info'] = f'{(ip6_info)}'
        #result['hostname'] = f'La dirección IP de {host_name} es {socket.gethostbyname(host_name)}'
        return result


class ServerInfoSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    def _get_current_frequency(self):
        try:
            return self.env['res.config.settings'].search_read([], ['update_frequency'])[-1][
                'update_frequency']
        except Exception as ex:
            _logger.error(f" {ex}")

        return '5000'

    update_frequency = fields.Selection(
        string='Time between updates',
        help='This value sets time between Server Info updates.',
        selection=[
            ('1000', '1 Sec'),
            ('2000', '2 Sec'),
            ('5000', '5 Sec'),
            ('10000', '10 Sec'),
            ('30000', '30 Sec'),
            ('60000', '1 Min'),
            ('300000', '5 Min')
        ],
        default=_get_current_frequency,
        required=True
    )
